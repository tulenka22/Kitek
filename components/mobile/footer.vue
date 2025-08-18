<template>
  <footer class="footer">
    <div class="footer__columns">
      <div class="column">
        <h1 class="column__title">Основная</h1>
        <p class="column__item">Главная</p>
        <p class="column__item">Новости</p>
        <p class="column__item">Контакты</p>
      </div>
      <span class="footer__separator footer__separator-vertical" />
      <div class="column column-right">
        <h1 class="column__title">Навигация</h1>
        <p class="column__item">Студенту</p>
        <p class="column__item">Абитуриенту</p>
        <p class="column__item">Преподавателю</p>
      </div>
    </div>
    <span class="footer__separator footer__separator-horizontal" />
    <div class="footer__content">
      <div class="footer__info">
        <p class="footer__p">Приемная директора: <a href="tel:68-07-73">68-07-73</a>;</p>
        <p class="footer__p">Приемная комиссия: <a href="tel:68-07-66">68-07-66</a>;</p>
        <p class="footer__p">Почта: <a href="mailto:tradeconomy@mail.ru">tradeconomy@mail.ru</a></p>
      </div>
      <div class="socials">
        <a href="https://vk.com/omsktec" class="icon socials__item" target="_blank">
          <icon-wrapper width="24" height="24"> <IconVK /> </icon-wrapper>
        </a>
        <!-- <a href="https://t.me/omskkitec" class="icon socials__item" target="_blank">
          <icon-wrapper width="24" height="24"> <IconTelegram /> </icon-wrapper>
        </a> -->
      </div>
    </div>
    <span class="footer__separator footer__separator-horizontal" />
    <div class="footer__copyright">
      <p class="footer__p">Колледж инновационных технологий, экономики и коммерции</p>
      <p class="footer__copyright__text">© 2024 Все права защищены.</p>
    </div>
  </footer>
</template>

<script>
export default {
  name: 'MobileFooter',
}
</script>

<style scoped lang="scss">
.footer {
  background-color: $primary-text-color;
  border-top: 1px solid $border-color;
  box-shadow: $footer-shadow;
  padding: 16px 12px;
  color: $bg-primary;
  &__columns {
    width: 100%;
    display: flex;
    justify-content: space-between;
    margin-bottom: 16px;
  }
  &__separator {
    background-color: $accent-color;
    box-shadow: 0px 0px 8px rgba(247, 157, 165, 0.4);
    display: block;
    &-vertical {
      width: 1px;
      height: auto;
    }
    &-horizontal {
      width: 100%;
      height: 1px;
    }
  }
  &__content {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 8px 0;
  }
  &__p {
    @include tg(15px, 400, 18px);
    margin-top: 6px;
    > a {
      text-decoration: underline;
      text-underline-offset: 1.2px;
    }
  }
  &__copyright {
    padding: 8px 0;
    text-align: center;

    &__text {
      margin-top: 10px;
      @include tg(10px, 400, 12px);
    }
  }
}

.socials {
  &__item {
    margin-bottom: 6px;
    &:last-child {
      margin-bottom: 0;
    }
  }
}

.column {
  &__title,
  &__item {
    margin-top: 4px;
    &:first-child {
      margin-top: 0;
    }
  }
  &__title {
    @include tg(18px, 600, 21px);
    color: $accent-color;
  }
  &__item {
    @include tg(13px, 500, 15px);
  }
  &-right {
    text-align: right;
  }
}
</style>
