
const Modelo = {
    async iniciarSesion(username, password) {
      const datos_insertar = {
        username: username,
        password: password
      }
      const res = await axios({
        method: "POST",
        url: "http://127.0.0.1:5000/login",
        data: datos_insertar
      });
      return res;
    }
  }
  
  const Vista = {
    getDatosIniciarSesion() {
      const username = document.getElementById('username').value;
      const password = document.getElementById('password').value;
      return { username, password };
    },
    getdatoredirigirindex(){
        
        location.href = ("../dashboard/admin.html");
    },
    mostrarMensajeError(mensaje) {
        console.log(mensaje);
        
          },
    mostrarMensajeSatisfactorio(mensaje) {
      console.log(mensaje);
    }

  }
  
  const Controlador = {
    async iniciarSesion() {
      const { username, password } = Vista.getDatosIniciarSesion();
      try {
        const res = await Modelo.iniciarSesion(username, password);
        console.log(res);
        if (res.data.acceso == "AUTORIZADO") {
          const access_token = res.data.access_token;
          localStorage.setItem("access_token", access_token);
          Vista.mostrarMensajeSatisfactorio("Inicio de sesión exitoso");
          Vista.getdatoredirigirindex();
        } else {
          Vista.mostrarMensajeError("Usuario no encontrado")
          Vista.limpiarCampos();
        }
      } catch(err) {
      Vista.mostrarMensajeError('Error al iniciar sesión');
      console.log(err);
  
    }
  }
  }
  
  
const botonIniciarSesion = document.getElementById('botonIniciarSesion');
  botonIniciarSesion.onclick = function () {
    Controlador.iniciarSesion()

  }




