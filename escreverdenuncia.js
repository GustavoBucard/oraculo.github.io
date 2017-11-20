window.onscroll = function() {scrollFunction()};

function scrollFunction() {
if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
  document.getElementById("nav2").style.display = "block";
  } else {
    document.getElementById("nav2").style.display = "none";
  }
}

// volta para o topo da página
function topFunction() {
  document.body.scrollTop = 0;  
  document.documentElement.scrollTop = 0; 
}

// computar os dados do formulario
var i = 0; // contador de envios
function enviar(){

  if (document.forms["formulario"]["denuncia"].value == "") {
    alert("Favor preencher o campo de denúncia.");
    return false;
  }

  var denuncia = document.forms["formulario"]["denuncia"].value;
  var frame =  denuncia;

  download(frame, "denuncia" + i);

  i++;

  alert("Parabéns, sua denuncia foi computada com sucesso!");

  return true;
}

function download(text, filename) {
  var array = new Array();
  array[0] = text;
  console.log(array, filename)
  var blob = new Blob(array, {type: "text/plain;charset=utf-8"});
  saveAs(blob, "denuncia" + ".html");
}

