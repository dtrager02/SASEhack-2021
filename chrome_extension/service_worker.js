const SERVER_ADDR = "http://137.184.111.100:8080";

function sendReportStatusToContentScript(isError) {
    // We assume the current active tab is 
    // where the reported message coming from
    chrome.tabs.query({active: true, currentWindow: true}).then(

        (tabs) => {
            chrome.tabs.sendMessage(tabs[0].id, {type: "reportMessage", success: isError}, 
                (response) => {
                    console.log(`Response from Content Script: ${response}`);
            });
        },

        (reason) => {
            console.error(`Failed to query current tab. ${reason}`)
        }
    )
}

/**
 * 
 * @param {chrome.contextMenus.OnClickData} data 
 * @param {chrome.tabs.Tab} tab 
 */
function reportSelectedText(data, tab) {
    const apiEndpoint = `${SERVER_ADDR}/api/hate/model/add?text=${data.selectionText}`

    fetch(apiEndpoint, {
        method: "post"
    })
    .then(json => json)
    .then((data) => {
        let parsed = JSON.parse(data);
        if (parsed.isError || !parsed.response.success)
        {
            sendReportStatusToContentScript(true);
        }
        else
        {
            sendReportStatusToContentScript(false);
        }
    })
    .catch((error) => {
        sendReportStatusToContentScript(true);
    });
}

// we only need to bind to the content menu once after install
chrome.runtime.onInstalled.addListener(() => {
    chrome.contextMenus.create({
        id: "report-text-clicked",
        title: "Report: %s",
        contexts: ["selection"]
    })    
})

chrome.contextMenus.onClicked.addListener(reportSelectedText)
