<template>
  <block-ab title="Студенту">
    <nav>
      <nuxt-link to="/student/grafiks" class="menu__link"> График учебного процесса </nuxt-link>
      <nuxt-link to="/student/schedule" class="menu__link"> Расписание занятий </nuxt-link>

      <nuxt-link to="/student/contests" class="menu__link">
        Конкурсы, олипиады, конференции
      </nuxt-link>

      <nuxt-link to="/student/sportclub" class="menu__link">
        Студенческий спортивный клуб «Старт»
      </nuxt-link>
      <nuxt-link to="/student/assistance" class="menu__link">
        Содействие трудоустройству выпускников
      </nuxt-link>
      <nuxt-link to="/student/remote" class="menu__link"> Дистанционное обучение </nuxt-link>
      <nuxt-link to="/student/sketchbook" class="menu__link"> "Скетчбук СПО" </nuxt-link>

      <nuxt-link to="/student/extramural" class="menu__link"> Заочное отделение </nuxt-link>
      <!-- <nuxt-link to="/student/parents" class="menu__link"> Материалы для родителей </nuxt-link> -->
      <nuxt-link to="/student/terror" class="menu__link">
        Противодействие терроризму и экстремизму
      </nuxt-link>
      <nuxt-link to="/student/railway" class="menu__link"> Железнодорожная безопасность </nuxt-link>
      <nuxt-link to="/student/safety" class="menu__link"> Пожарная безопасность </nuxt-link>
      <nuxt-link to="/student/mediacenter" class="menu__link"
        >Медиацентр «В ОБЪЕКТИВЕ КИТЭКА»</nuxt-link
      >
      <nuxt-link to="/student/professionalitet" class="menu__link"
        >Теперь мы в "Профессионалитете"!</nuxt-link
      >
      <nuxt-link to="/student/livestudent" class="menu__link"
        >Студенческая жизнь: открывай мир, твори будущее!</nuxt-link
      >
    </nav>
  </block-ab>
</template>

<script>
export default {}
</script>

<style scoped lang="scss">
@import '~/assets/common';
</style>
