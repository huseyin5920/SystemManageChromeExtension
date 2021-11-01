const notify = document.getElementById( 'connect' );

notify.addEventListener( 'click', () => {
  console.log("basıldı")
  // var newURL = "localhost:3000";
  // chrome.tabs.create({ url: newURL });

  window.open("index.html") 
} );