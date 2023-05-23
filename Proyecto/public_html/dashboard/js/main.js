//recargar la tabla de la gestion de contactos.
document.addEventListener("DOMContentLoaded", function() {
    const csvTable = document.getElementById("tablaPersonas").getElementsByTagName('tbody')[0];

    // Función para eliminar filas anteriores y cargar nuevos datos
    function actualizarTabla() {
        // Eliminar filas anteriores
        while (csvTable.firstChild) {
            csvTable.removeChild(csvTable.firstChild);
        }

        fetch("http://127.0.0.1:5000/getcontactos")
            .then(response => response.json())
            .then(data => {
                data.forEach(csv => {
                    const row = csvTable.insertRow(-1);
                    const id = row.insertCell(0);
                    const nombre = row.insertCell(1);
                    const apellido = row.insertCell(2);
                    const correo = row.insertCell(3);
                    const telefono = row.insertCell(4);

                    id.innerHTML = csv.id;
                    nombre.innerHTML = csv.nombre;
                    apellido.innerHTML = csv.apellido;
                    correo.innerHTML = csv.correo;
                    telefono.innerHTML = csv.telefono;
                });
            });

        console.log("Datos actualizados");
    }

    // Llamar a la función cuando se carga la página
    actualizarTabla();
});
//recargar la tabla de la data.
document.addEventListener("DOMContentLoaded", function() {
    const csvTable = document.getElementById("tablacsv").getElementsByTagName('tbody')[0];

    // Función para eliminar filas anteriores y cargar nuevos datos
    function actualizarTabla() {
        // Eliminar filas anteriores
        while (csvTable.firstChild) {
            csvTable.removeChild(csvTable.firstChild);
        }

        fetch("http://127.0.0.1:5000/getcsv")
            .then(response => response.json())
            .then(data => {
                data.forEach(csv => {
                    const row = csvTable.insertRow(-1);
                    const edad = row.insertCell(0);
                    const trabajo = row.insertCell(1);
                    const civil = row.insertCell(2);
                    const educacion = row.insertCell(3);
                    const credito = row.insertCell(4);
                    const vivienda = row.insertCell(5);
                    const prestamo = row.insertCell(6);
                    const contacto = row.insertCell(7);
                    const mes = row.insertCell(8);
                    const ultimasemana = row.insertCell(9);
                    const duracion = row.insertCell(10);
                    const campa = row.insertCell(11);
                    const numdiascontacto = row.insertCell(12);
                    const anterior = row.insertCell(13);
                    const resulmarkanterior = row.insertCell(14);
                    const tasavariempleo = row.insertCell(15);
                    const indpreconsumo = row.insertCell(16);
                    const indconfconsumo = row.insertCell(17);
                    const euribor3m = row.insertCell(18);
                    const nempleados = row.insertCell(19);
                    const suscrito = row.insertCell(20);
                    

                    edad.innerHTML = csv.edad;
                    trabajo.innerHTML = csv.trabajo;
                    civil.innerHTML = csv.civil;
                    educacion.innerHTML = csv.educacion;
                    credito.innerHTML = csv.credito;
                    vivienda.innerHTML = csv.vivienda;
                    prestamo.innerHTML = csv.prestamo;
                    contacto.innerHTML = csv.contacto;
                    mes.innerHTML = csv.mes;
                    ultimasemana.innerHTML = csv.ultimasemana;
                    duracion.innerHTML = csv.duracion;
                    campa.innerHTML = csv.campa;
                    numdiascontacto.innerHTML = csv.numdiascontacto;
                    anterior.innerHTML = csv.anterior;
                    resulmarkanterior.innerHTML = csv.resulmarkanterior;
                    tasavariempleo.innerHTML = csv.tasavariempleo;
                    indpreconsumo.innerHTML = csv.indpreconsumo;
                    indconfconsumo.innerHTML = csv.indconfconsumo;
                    euribor3m.innerHTML = csv.euribor3m;
                    nempleados.innerHTML = csv.nempleados;
                    suscrito.innerHTML = csv.suscrito;
                });
            });

        console.log("Datos actualizados");
    }

    // Llamar a la función cuando se carga la página
    actualizarTabla();
});
//funcion para cargar la tabla.
function loadTable(){
    const csvTable = document.getElementById("tablaPersonas").getElementsByTagName('tbody')[0];
    // Eliminar filas anteriores
    while (csvTable.firstChild) {
        csvTable.removeChild(csvTable.firstChild);
    }
    fetch("http://127.0.0.1:5000/getcontactos")
        .then(response => response.json())
        .then(data => {
            data.forEach(csv => {
                const row = csvTable.insertRow(-1);
                const id = row.insertCell(0);
                const nombre = row.insertCell(1);
                const apellido = row.insertCell(2);
                const correo = row.insertCell(3);
                const telefono = row.insertCell(4);
               
                
                id.innerHTML = csv.id;
                nombre.innerHTML = csv.nombre;
                apellido.innerHTML = csv.apellido;
                correo.innerHTML = csv.correo;
                telefono.innerHTML = csv.telefono;
               
                
            });
        });
  console.log("Haz hecho clic en el botón!");

}
//boton para consultar.
var miBoton = document.getElementById("BtnConsultar");
miBoton.addEventListener("click", function() {
    loadTable();
});

// codigo para eliminar registro en gestion de contactos.
var deleteButton = document.getElementById('BtnDelete');
deleteButton.addEventListener('click', function() {
    
    var cajadetexto = document.getElementById('idDelete').value;
   
    fetch('http://127.0.0.1:5000/eliminarcontactos', {
        method: 'POST',
        body: JSON.stringify({
            id: cajadetexto

        }),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => {
        if (response.ok) {
            document.getElementById('idDelete').value = ''; // Borrar el valor de la caja de texto
            location.reload(); // Recargar la página
        } else {
            throw new Error('Error al eliminar el contacto.');
        }
    })
    .catch(error => console.error(error));
    
});

// codigo para eliminar registro de la tabla data.
var deleteButton = document.getElementById('eliminarbtn');
deleteButton.addEventListener('click', function() {
    
    var cajadetexto = document.getElementById('elimirartxt').value;
   
    fetch('http://127.0.0.1:5000/', {
        method: 'POST',
        body: JSON.stringify({
            id: cajadetexto

        }),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => {
        if (response.ok) {
            document.getElementById('idDelete').value = ''; // Borrar el valor de la caja de texto
            location.reload(); // Recargar la página
        } else {
            throw new Error('Error al eliminar el contacto.');
        }
    })
    .catch(error => console.error(error));
    
});

//function abrirventana(){
//    window.location.href = 'insertar.html';
//}

