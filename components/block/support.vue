<template>
  <div class="suport">
    <a href="https://pobeda.onf.ru/" target="_blank">
      <img class="help" src="/img/help1.png" alt="https://pobeda.onf.ru/" />
      <img class="help__mobile" src="/img/help2.png" alt="https://pobeda.onf.ru/" />
    </a>
  </div>
</template>

<script></script>

<style scoped lang="scss">
.suport {
  width: 100%;
  margin-top: 20px;
}
.help {
  width: 100vw;
  max-height: 21vw;
  @media screen and (max-width: 640px) {
    display: none;
  }
  &__mobile {
    display: none;
    @media screen and (max-width: 640px) {
      display: block;
      max-width: 240px;
      max-height: 400px;
      margin-left: auto;
      margin-right: auto;
    }
  }
}
</style>
