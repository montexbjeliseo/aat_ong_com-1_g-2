function editar(id){
    let comentario = document.getElementById("id_comentario"+id);
    let formulario = document.getElementById("id_texto"+id);
    comentario.classList.toggle("d-none");
    formulario.classList.toggle("d-block");
    comentario.classList.remove("d-block");
    formulario.classList.remove("d-none");
}

function cancelar_edicion(id){
    let comentario = document.getElementById("id_comentario"+id);
    let formulario = document.getElementById("id_texto"+id);
    comentario.classList.toggle("d-block");
    formulario.classList.toggle("d-none");
    comentario.classList.remove("d-none");
    formulario.classList.remove("d-block");
}