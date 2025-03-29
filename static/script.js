function openTab(tabId) {
    // Hide all tab contents
    var tabs = document.querySelectorAll('.tab-content');
    tabs.forEach(function(tab) {
        tab.style.display = 'none';
    });

    // Show the selected tab
    var selectedTab = document.getElementById(tabId);
    if (selectedTab) {
        selectedTab.style.display = 'block';
    }
}

// Optionally, you can set a default tab to show
document.addEventListener('DOMContentLoaded', function() {
    openTab('keylogger'); // Set default tab
});
