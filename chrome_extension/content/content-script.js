function injectPopoverElement() {
    let url = chrome.runtime.getURL("content/inject/mouse_popover.html")
    fetch(url).then((response) => {
        return response.text();
    }).then(html => {
        document.body.insertAdjacentHTML("afterbegin", html);
    });
}

function createSendSuccessPopover() {
    let messageElement = document.getElementById("api-ext-mouse-popover-msg");
    messageElement.classList.remove("api-ext-mouse-popover-hidden");
    messageElement.classList.remove("api-ext-popover-fail");
    messageElement.classList.add("api-ext-popover-success");
    
    setTimeout(() => {
        messageElement.classList.add("api-ext-mouse-popover-hidden"); 
    }, 3000);
}

function createSendFailPopover() {
    let messageElement = document.getElementById("api-ext-mouse-popover-msg");
    messageElement.classList.remove("api-ext-mouse-popover-hidden");
    messageElement.classList.remove("api-ext-popover-success");
    messageElement.classList.add("api-ext-popover-fail");
    
    setTimeout(() => {
        messageElement.classList.add("api-ext-mouse-popover-hidden"); 
    }, 3000);
}

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    // Noticed the use of ?. operator (Optional chaining)
    // Instead of raising an error when type does not exist on message
    // ?. makes it return null, so the code will still continue to execute w/o error handling
    if (message?.type === "reportMessage") {
        console.log("hi")
        createSendSuccessPopover();
    }
});

window.addEventListener("load", () => {
    injectPopoverElement();
});
