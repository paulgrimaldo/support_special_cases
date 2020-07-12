<template>
  <footer class="footer bg-dark">
    <div class="container text-white">
      <div class="row justify-content-md-center">
        <div class="col-lg-4 col-md-6 col-sm-12">
          <h5 class="text-center">Acerca de Support Ficct
            <img src="../assets/support_logo.svg" alt="SupportFicct" width="32px" height="32px">
          </h5>
          <p>
            Grupo de apoyo a los estudiantes, buscando un cambio innovador y promoviendo el desarrollo y crecimiento de
            la F.I.C.C.T
          </p>

        </div>
        <div class="col-lg-4 col-md-6 col-sm-12">
          <h5 class="text-center">Enlaces &uacute;tiles</h5>
          <ul>
            <li><a href="/">Inicio</a></li>
            <li><a href="/acerca-de">Acerca de</a></li>
            <li><a target="_blank" href="http://supportficct.somee.com/">P&aacute;gina oficial</a></li>
          </ul>
        </div>
        <div class="col-lg-4 col-md-6 col-sm-12">
          <h5 class="text-center">Contacto</h5>
          <ul>
            <li>
              <i class="fas fa-map-marker-alt" style="color: red"></i>
              U.A.G.R.M M&oacute;dulo 236
            </li>
            <li>
              <a href="tel:+59169000850">
                <i class="fas fa-mobile-alt"></i> (+591) 690-008-50
              </a>
            </li>
            <li>
              <a href="mailto:paulgrimaldobravo@gmail.com?subject=Acerca de SupportFicct!">
                <i class="far fa-envelope"></i>
                paulgrimaldobravo@gmail.com
              </a>
            </li>
            <li class="text-center">
              <a href="https://www.facebook.com/supportUAGRM" target="_blank">
                <i class="fab fa-facebook-square"></i>
              </a>
              <a href="https://api.whatsapp.com/send?phone=59169000850" class="ml-2" target="_blank">
                <i class="fab fa-whatsapp"></i>
              </a>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </footer>
</template>

<script>
  export default {};
</script>

<style scoped>
  .footer {
    width: 100%;
    margin-top: 60px;
  }

  .footer > .container {
    padding-right: 15px;
    padding-left: 15px;
    padding-top: 15px;
    margin-bottom: 0;
  }

  .footer ul {
    list-style: none;
  }

  .footer a {
    color: white;
  }

  .footer a:hover {
    color: white;
    text-decoration: none;
  }
</style>
