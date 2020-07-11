<template>
  <transition>
    <template v-if="template === 'student_detail'">
      <transition>
        <template v-if="careersData != null">
          <student-detail></student-detail>
        </template>
        <template v-else>
          <loading-indicator></loading-indicator>
        </template>
      </transition>
    </template>
    <template v-else-if="template === 'classes_selector'">
      <classes-selector></classes-selector>
    </template>
    <template v-else-if="template === 'groups_selector'">
      <groups-selector></groups-selector>
    </template>
    <template v-else-if="template === 'sending_special_case_data'">
      <loading-indicator></loading-indicator>
    </template>
    <template v-else>
      <process-summary></process-summary>
    </template>
  </transition>
</template>

<script>
  import {mapActions, mapState} from 'vuex';

  export default {
    computed: mapState([
      'studentData',
      'studentCareerData',
      'careersData',
      'template',
    ]),
    methods: mapActions(['getCareers']),
    created() {
      this.getCareers();
    }
  };
</script>

<style>
</style>
