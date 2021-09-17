const app = new Vue({
    delimiters: ["[[", "]]"],
    el: '#mainContent',
    data: {
        titulo: 0,
        mes:'',
        year:'Selecciona el año',
        urls:'',
        datos: []
    },

    methods: {
        hitoseleccionado() {
            this.urls = localStorage.getItem("url");
            axios.post(this.urls+"hitos"+"/"+this.year+"/"+this.mes)
            .then(response => {
                this.datos = response.data.obras;
                $("#hito").hide('slow');   
                this.datos.forEach(element => {
                });
            }).catch(error => {
            });
        }
    }
  });
