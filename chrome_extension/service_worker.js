function sendReportSuccessToContentScript() {
    // We assume the current active tab is 
    // where the reported message coming from
    chrome.tabs.query({active: true, currentWindow: true}).then(

        (tabs) => {
            chrome.tabs.sendMessage(tabs[0].id, {type: "reportMessage", success: true}, 
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
    console.log(data.selectionText)

    sendReportSuccessToContentScript()
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
