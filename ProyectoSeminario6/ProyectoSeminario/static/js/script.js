$(document).ready(inicio)
function inicio()
{
	$("#formulario :input").blur(validar);
}
function validar(){
	
	if(this.id=='id_username'){
		var tusuario=this.value;
		$.ajax({
			type:'POST',
			url:'/verificar/',
			data:$('#formulario').serialize(),
			beforeSend: antesEnviar,
			success: llegada,
			error:errores
			});
	}
}
function antesEnviar(){
	$("#resultado").text("Verificando...");
}
function llegada(data){
	$("#resultado").text(data);
}
function errores(){
	$("#resultado").text("Problemas en el servidor...");
}