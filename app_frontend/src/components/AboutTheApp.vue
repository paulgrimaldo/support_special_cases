<template>
  <section>
    <article class="row">
      <div class="col-lg-6 col-md-6 col-sm-12 order-md-2 text-center">
        <img src="../assets/support_ficct.png" alt="SupportFicct" class="img-logo">
      </div>
      <div class="col-lg-6 col-md-6 col-sm-12 order-md-1">
        <h1>Support Ficct generador de documentos para casos especiales</h1>
        <p class="lead">
          Esta herramienta te permite introducir tus datos b&aacute;sicos como estudiante, seleccionar tus materias
          aprobadas, inscritas y las que deseas hacer como caso especial, elegir los grupos para tus materias de caso
          especial y generar toda la documentaci&oacute;n para tu tr&aacute;mite
        </p>
        <div class="d-flex flex-column flex-md-row">
          <a href="#" class="btn btn-lg btn-outline-primary mb-3">
            <router-link class="nav-link" to="/">Iniciar</router-link>
          </a>
        </div>
        <p class="text-muted mb-0">
          Actualmente v1.0
        </p>
      </div>
    </article>
    <article class="row mt-5 align-items-center">
      <div class="col-md-5">
        <h2>Datos estudiantiles</h2>
        <p class="lead font-weight-normal">Genera tus documentos con los datos de tu universidad</p>
      </div>
      <div class="col-md-7">
        <img src="../assets/student_detail.png" alt="Student details" class="description-img">
      </div>
    </article>
    <article class="row mt-5 align-items-center">
      <div class="col-md-7">
        <img src="../assets/classes_selector.png" alt="Classes Selector" class="description-img">
      </div>
      <div class="col-md-5">
        <h2>Selector de materias</h2>
        <p class="lead font-weight-normal">
          Selecciona tus materias aprobadas, tus materias inscritas en la presente gesti&oacute;n y las materias que
          quieres realizar como caso especial.
        </p>
        <p>Cada tipo de materia (Aprobada,Inscrita,Caso especial) puede seleccionarse con un color diferente</p>
      </div>
    </article>
    <article class="row mt-5 align-items-center">
      <div class="col-md-5">
        <h2>Selector de grupos</h2>
        <p class="lear font-weight-normal">
          Ingresa los grupos de las materias que quieres hacer como caso especial.
        </p>
      </div>
      <div class="col-md-7">
        <img src="../assets/groups_selector.png" alt="Groups Selector" class="description-img">
      </div>
    </article>
    <article class="row mt-5 align-items-center">
      <div class="col-md-7">
        <img src="../assets/docs_generated.png" alt="Docs Generated" class="description-img">
      </div>
      <div class="col-md-5">
        <h2>Documentos en PDF</h2>
        <p class="lear font-weight-normal">
          Obt&eacute;n un archivo .zip con todos los documentos en formato PDF para que puedas seguir con tus
          tr&aacute;mites de caso especial.
        </p>
      </div>
    </article>

    <article class="row mt-5 justify-content-center">
      <h2 style="width: 100%" class="text-center">
        Desarrollado por el equipo Support
      </h2>
      <div class="col-lg-4 col-md-6 col-sm-6 d-flex align-items-stretch mt-4">
        <div class="shadow card h-100" style="width: 18rem; margin: 0 auto">
          <img src="../assets/paul_grimaldo.jpg" class="card-img-top" alt="Paul Grimaldo">
          <div class="card-body">
            <h5 class="card-title">Paul Grimaldo</h5>
            <p class="card-text">
              El verdadero progreso es el que pone la tecnología al alcance de todos
            </p>
          </div>
        </div>
      </div>
      <div class="col-lg-4 col-md-6 col-sm-6 d-flex align-items-stretch mt-4">
        <div class="shadow card h-100" style="width: 18rem; margin: 0 auto">
          <img src="../assets/ronaldo_rivero.jpg" class="card-img-top" alt="Ronaldo Rivero">
          <div class="card-body">
            <h5 class="card-title">Ronaldo Rivero</h5>
            <p class="card-text">
              Dispuesto a ayudar a los compañeros de la FICCT
            </p>
          </div>
        </div>
      </div>
      <div class="col-lg-4 col-md-6 col-sm-6 d-flex align-items-stretch mt-4">
        <div class="shadow card h-100" style="width: 18rem; margin: 0 auto">
          <img src="../assets/jhafeth_cadima.jpg" class="card-img-top" alt="Jhafeth Cadima">
          <div class="card-body">
            <h5 class="card-title">Jhafeth Cadima</h5>
            <p class="card-text">
              Estudia y venceras, amigo de todos y bailar&iacute;n de la FICCT
            </p>
          </div>
        </div>
      </div>
      <div class="col-lg-4 col-md-6 col-sm-6 d-flex align-items-stretch mt-4">
        <div class="shadow card h-100" style="width: 18rem; margin: 0 auto">
          <img src="../assets/alejandro_loma.jpg" class="card-img-top" alt="Alejandro Loma">
          <div class="card-body">
            <h5 class="card-title">Alejandro Loma</h5>
            <p class="card-text">
              Es intentando lo imposible como se realiza lo posible
            </p>
          </div>
        </div>
      </div>
      <div class="col-lg-4 col-md-6 col-sm-6 d-flex align-items-stretch mt-4">
        <div class="shadow card h-100" style="width: 18rem; margin: 0 auto">
          <img src="../assets/team_support.jpg" class="card-img-top" alt="Equipo Support">
          <div class="card-body">
            <h5 class="card-title">Equipo support</h5>
            <p class="card-text">
              1000+ integrantes
            </p>
          </div>
        </div>
      </div>
    </article>
  </section>
</template>

<script>
  export default {}
</script>

<style scoped>
  .img-logo {
    max-width: 100%;
  }

  .description-img {
    border-radius: 5px;
    box-shadow: 5px 5px 5px rgba(0, 0, 0, 0.3);
    width: 100%;
  }
</style>
