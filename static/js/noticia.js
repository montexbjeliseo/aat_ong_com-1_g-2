function alternar_visibilidad_nueva_categoria(){
    let elemento = document.getElementById("id_categoria");
    let nueva_categoria_campo = document.getElementById("id_nueva_categoria");
    if (elemento.value === "" && nueva_categoria_campo.classList.contains("d-none")){
        nueva_categoria_campo.classList.remove("d-none");
    } else if(!nueva_categoria_campo.classList.contains("d-none")) {
        nueva_categoria_campo.classList.toggle("d-none");
    }
}