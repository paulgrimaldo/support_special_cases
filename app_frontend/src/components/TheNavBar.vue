<template>
  <header>
    <nav class="navbar navbar-expand-lg navbar-light static-top">
      <div class="container">
        <a class="navbar-brand" href="/">
          <img src="../assets/support_logo.svg" width="48px" height="48px" alt="Support Ficct"/>
          Support Ficct
        </a>
        <button
          class="navbar-toggler"
          type="button"
          data-toggle="collapse"
          data-target="#navbarResponsive"
          aria-controls="navbarResponsive"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarResponsive">
          <ul class="navbar-nav ml-auto">
            <li class="nav-item active">
              <router-link class="nav-link" to="/">Inicio</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/acerca-de">Acerca de</router-link>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="mailto:paulgrimaldobravo@gmail.com?subject=Acerca de SupportFicct!"
                 target="_blank">
                Contacto
              </a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </header>
</template>

<script>
  export default {};
</script>

<style>
</style>
