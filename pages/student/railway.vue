<template>
  <block-ab title="Железнодорожная безопасность">
    <h2 class="ab__subtitle" style="margin-top: 0px">
      Основные причины детского и юношеского травматизма
    </h2>
    <div class="ab__video">
      <video class="ab__video" controls>
        <source src="/video/Безопасность на жд2023.mp4" type="video/mp4" />
        Ваш браузер не поддерживает видео
      </video>
    </div>
    <a
      class="pdf-link"
      target="_blank"
      href="/data/safety/Приложение № 1 листовки по безопасности.pdf">
      <img src="/img/safety/Приложение 1.jpg" />
      <div class="pdf-link-background"><b class="test" red>▼ Подробнее ▼</b></div>
    </a>
    <a
      class="pdf-link"
      target="_blank"
      href="/data/safety/Приложение № 2 листовки по безопасности.pdf">
      <img src="/img/safety/Приложение 2.jpg" />
      <div class="pdf-link-background">
        <b style="bottom: 30px" class="test" red>▼ Подробнее ▼</b>
      </div>
    </a>
    <common-documents-list json-path="documents/railway.json" />
  </block-ab>
</template>

<script>
export default {}
</script>

<style scoped lang="scss">
.ab {
  &__video {
    margin: 10px;
    margin-left: auto;
    margin-right: auto;
    max-width: 580px;
    max-height: auto;
    @include small-media() {
      max-width: 260px;
      max-height: auto;
    }
  }
}
.pdf-link {
  position: relative;
  display: block;
  max-width: 600px;
  height: auto;
  margin: 5vw;

  &-background {
    z-index: 100;
    position: absolute;
    top: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(rgba(0, 0, 0, 0), 80%, rgb(255, 254, 254));
  }
}
.test {
  position: absolute;
  bottom: 80px;
  left: 40%;
  @include small-media() {
    left: 30%;
  }
}
</style>
