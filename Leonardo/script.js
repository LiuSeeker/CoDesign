document.addEventListener("DOMContentLoaded", function() {


  var troca = function() {
  	var x = Math.floor((Math.random() * 10) + 1);
    var foto = document.querySelector(".foto");

    foto.src = "img/all/" + x + ".png";

  }

  setInterval(troca, 4500);

});

document.addEventListener("DOMContentLoaded", function() {


  var troca = function() {
  	var x = Math.floor((Math.random() * 10) + 1);
    var foto2 = document.querySelector(".foto2");

    foto2.src = "img/all/" + x + ".png";

  }

  setInterval(troca, 4000);

});

document.addEventListener("DOMContentLoaded", function() {

  var troca = function() {
  	var x = Math.floor((Math.random() * 10) + 1);
    var foto3 = document.querySelector(".foto3");

    foto3.src = "img/all/" + x + ".png";

  }

  setInterval(troca, 5000);

});

document.addEventListener("DOMContentLoaded", function() {

  var troca = function() {
  	var x = Math.floor((Math.random() * 10) + 1);
    var foto3 = document.querySelector(".foto3");

    foto3.src = "img/all/" + x + ".png";

  }

});

function random_link(){
    var myrandom=Math.round(Math.random()*13)
    var link1="acel.html"
    var link2="artigo.html"
    var link3="brinquedo.html"
    var link4="case.html"
    var link5="chuveiro.html"
    var link6="dinpop.html"
    var link7="estacao.html"
    var link8="inspermon.html"
    var link9="leitor.html"
    var link10="manufatura.html"
    var link11="petroleo.html"
    var link12="pygame.html"
    var link13="termofarmaco.html"
    var link14="tweet.html"
    if (myrandom==0)
        window.location=link1
    else if (myrandom==1)
        window.location=link2
    else if (myrandom==2)
        window.location=link3
    else if (myrandom==3)
        window.location=link4
    else if (myrandom==4)
        window.location=link5
    else if (myrandom==5)
        window.location=link6
    else if (myrandom==6)
        window.location=link7
    else if (myrandom==7)
        window.location=link8
    else if (myrandom==8)
        window.location=link9
    else if (myrandom==9)
        window.location=link10
    else if (myrandom==10)
        window.location=link11
    else if (myrandom==11)
        window.location=link12
    else if (myrandom==12)
        window.location=link13
    else if (myrandom==13)
        window.location=link14
}