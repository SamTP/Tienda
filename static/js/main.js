function subtotal(params) {
  cnt=parseInt(document.getElementById("id_cantidad").value);
  prc=parseFloat(document.getElementById("id_precio").value);
  document.getElementById("id_total").value=cnt*prc;
}
