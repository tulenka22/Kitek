<template>
  <footer class="footer footer__group" v-if="!isMobile">
    <div class="footer__vertical footer__left">
      <div class="footer__group footer__group-fluid">
        <div class="column">
          <h2 class="column__title">Навигация</h2>
          <nuxt-link to="/" class="column__item"> Главная </nuxt-link>
          <nuxt-link to="/news" class="column__item"> Новости </nuxt-link>
          <nuxt-link to="/organization" class="column__item"> Об организации</nuxt-link>
        </div>
        <div class="column column-without-title">
          <nuxt-link to="/projects/projects-menu" class="column__item"> Проекты </nuxt-link>
          <nuxt-link to="/specialties" class="column__item"> Специальности </nuxt-link>
          <nuxt-link to="/teacher/useful-links" class="column__item"> Полезные ссылки </nuxt-link>
        </div>
        <div class="column column-without-title">
          <nuxt-link to="/student/student-menu" class="column__item"> Студенту </nuxt-link>
          <nuxt-link to="/enrolle/enrolle-menu" class="column__item"> Абитуриенту </nuxt-link>
          <nuxt-link to="/teacher/teacher-menu" class="column__item"> Преподавателю </nuxt-link>
        </div>
      </div>
      <span class="footer__separator footer__separator-horizontal" />
      <div class="copyright">
        <h2 class="copyright__title">
          Колледж инновационных технологий, экономики <br />и коммерции
        </h2>
        <h3 class="copyright__subtitle">© 2024 Все права защищены.</h3>
      </div>
    </div>
    <span class="footer__separator footer__separator-vertical" />
    <div class="footer__vertical footer__right">
      <div class="footer__group footer__group-fluid">
        <div class="column">
          <h2 class="column__title">Информация о корпусах</h2>
          <p class="column__item">Административный</p>
          <p class="column__item">ул. 27-я Северная, 69</p>
          <p class="column__item">Приёмная директора: <a href="tel:68-07-73">68-07-73</a></p>
        </div>
        <div class="column column-without-title">
          <p class="column__item">Корпус №2</p>
          <p class="column__item">ул. 24-я Северная, 123Б</p>
          <p class="column__item">Телефон: <a href="tel:68-26-77">68-26-77</a></p>
        </div>
        <div class="column column-without-title">
          <p class="column__item">Корпус №3</p>
          <p class="column__item">ул. 24-я Северная, 121</p>
          <p class="column__item">Телефон: <a href="tel:68-25-28">68-25-28</a></p>
        </div>
        <div class="column column-without-title">
          <p class="column__item">Отделение водного транспорта:</p>
          <p class="column__item">ул. Красный путь, 143</p>
          <p class="column__item">Телефон: <a href="tel:24-23-08">24-23-08</a></p>
        </div>
      </div>
      <span class="footer__separator footer__separator-horizontal" />
    </div>
  </footer>
  <MobileFooter v-else />
</template>

<script>
import { isMobile } from '~/core/utils/flags'
export default {
  name: 'AppFooter',
  computed: {
    isMobile() {
      return isMobile()
    },
  },
}
</script>

<style scoped lang="scss">
.footer {
  overflow: hidden;
  width: 100%;
  background-color: $primary-text-color;
  border-top: 1px solid $border-color;
  box-shadow: $footer-shadow;
  margin-top: 60px;
  &__group {
    display: flex;
    &-fluid {
      width: 100%;
      justify-content: space-between;
    }
  }
  &__left {
    width: 35%;
  }
  &__right {
    width: 65%;
  }
  &__vertical {
    padding: 24px;
  }
  &__separator {
    display: block;
    background-color: $accent-color;
    box-shadow: 0px 0px 8px rgba(247, 157, 165, 0.4);
    flex: none;
    &-vertical {
      height: auto;
      width: 2px;
    }
    &-horizontal {
      margin-top: 18px;
      width: 100%;
      height: 2px;
    }
  }
}
.column {
  white-space: nowrap;
  &:last-child {
    margin-right: 40px;
  }
  &__title {
    @include tg(22px, 700, 30px);
    color: $accent-color;
    @include high-media {
      font-size: 20px;
    }
    @include high-medium-media {
      font-size: 18px;
    }
  }
  &__item {
    display: block;
    @include tg(18px, 400, 25px);
    margin-top: 12px;
    color: $bg-control;
    white-space: nowrap;
    @include high-media {
      font-size: 16px;
    }
    @include high-medium-media {
      font-size: 14px;
    }
  }
  &-without-title {
    margin-top: 32px;
  }
}

.copyright {
  text-align: left;
  color: $bg-control;
  white-space: nowrap;
  &__title {
    margin-top: 16px;
    @include tg(14px, 400, 22px, 1px);
  }
  &__subtitle {
    margin-top: 8px;
    @include tg(12px, 400, 22px, 1px);
    > a {
      text-decoration: underline;
      text-decoration-style: dashed;
      text-underline-offset: 1px;
    }
  }
}
</style>
