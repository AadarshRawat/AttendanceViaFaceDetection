
  //get button
  var mybutton = document.getElementById("myBtn");
  
  // button display on/off when scroll
  window.onscroll = function() {scrollFunction()};
  
  function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
      mybutton.style.display = "block";
    } else {
      mybutton.style.display = "none";
    }
  }
  
  //  scroll to the top 
  function topFunction() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
  }
 //button
  var p=document.getElementById('attendance-button')

  function message(){
    alert('Excel File Will Be Downloaded')
  }



const links=document.querySelectorAll(".link-sound");
links.forEach(function(link){link.addEventListener("click", function(){
  console.log("Pressed");
  var audio=new Audio("{% static '/js/mixkit-gate-latch-click-1924.mp3' %}");
  audio.play();
})
});


