function subtotal(params) {
  cnt=parseInt(document.getElementById("id_cantidad").value);
  prc=parseFloat(document.getElementById("id_precio").value);
  document.getElementById("id_total").value=cnt*prc;
  if(cnt==0){
    document.getElementById("btn").disabled =true;
  }else{
    document.getElementById("btn").disabled =false;
  }
}
function cerrar(params) {
  document.getElementById("msg").style.display="none";
}