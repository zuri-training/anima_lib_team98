var acc = document.getElementsByClassName("accordion");
var i;

for (i = 0; i < acc.length; i++) {
  acc[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var panel = this.nextElementSibling;
    if (panel.style.display === "block") {
      panel.style.display = "none";
    } else {
      panel.style.display = "block";
    }
  });
}


function copyFunction() {
  const copyText = document.getElementById("copy_code_text").textContent;
  const textArea = document.createElement('textarea');
  textArea.textContent = copyText;
  document.body.append(textArea);
  textArea.select();
  textContent = copyText;
  document.execCommand("copy");
  textArea.remove();
  }
  document.getElementById('copy_code_button').addEventListener('click', copyFunction);


function startRating(item){
	rate=item.id[0];
	sessionStorage.star = rate;
	for(var i=0;i<5;i++){
		if(i<rate){
			document.getElementById((i+1)).style.color="purple";
		}
		else{
			document.getElementById((i+1)).style.color="ash";
		}
	}
}
