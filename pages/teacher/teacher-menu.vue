<template>
  <block-ab title="Преподавателю">
    <nav>
      <nuxt-link to="/teacher/certificate" class="menu__link"> Аттестация </nuxt-link>
      <nuxt-link to="/teacher/training" class="menu__link"> Повышение квалификации </nuxt-link>

      <nuxt-link to="/teacher/contests" class="menu__link"> Конкурсы </nuxt-link>

      <nuxt-link to="/teacher/useful-links" class="menu__link"> Полезные ссылки </nuxt-link>
    </nav>
  </block-ab>
</template>

<script>
export default {}
</script>

<style scoped lang="scss">
@import '~/assets/common';
</style>
