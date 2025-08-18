<template>
  <block-ab title="Пожарная безопасность">
    <h2 class="ab__subtitle" style="margin-top: 0px">Действия при пожаре</h2>
    <div class="ab__video">
      <video class="ab__video" controls>
        <source src="/video/Действия при пожаре.mp4" type="video/mp4" />
        Ваш браузер не поддерживает видео
      </video>
    </div>
    <h2 class="ab__subtitle" style="margin-top: 0px">Лайфхак МЧС эвакуация</h2>
    <div class="ab__video">
      <video class="ab__video" controls>
        <source src="/video/Лайфхак МЧС_ эвакуация.mp4" type="video/mp4" />
        Ваш браузер не поддерживает видео
      </video>
    </div>
    <h2 class="ab__subtitle" style="margin-top: 0px">ЧС пожар в квартире</h2>
    <div class="ab__video">
      <video class="ab__video" controls>
        <source src="/video/ЧС пожар в квартире.mp4" type="video/mp4" />
        Ваш браузер не поддерживает видео
      </video>
    </div>
    <h2 class="ab__subtitle" style="margin-top: 0px">Электроприборы</h2>
    <div class="ab__video">
      <video class="ab__video" controls>
        <source src="/video/Электроприборы.mp4" type="video/mp4" />
        Ваш браузер не поддерживает видео
      </video>
    </div>
    <common-documents-list json-path="documents/safety.json" />
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
</style>
