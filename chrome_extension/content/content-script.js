function createSendSuccessPopup() {
    
}

function createSendFailPopup() {
    
}

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    // Noticed the use of ?. operator.
    // Instead of raising an error when type does not exist on message
    // ?. makes it return null, so the code will still continue to execute w/o error handling
    if (message?.type === "reportMessage") {
        confirm("Hi");
    }
});
