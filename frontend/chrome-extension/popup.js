const notify = document.getElementById( 'connect' );

console.log("deneme")

notify.addEventListener( 'click', () => {
  console.log("basıldı")
  // var newURL = "localhost:3000";
  // chrome.tabs.create({ url: newURL });

  window.open("index.html") 
} );