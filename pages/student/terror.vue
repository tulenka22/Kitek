<template>
  <block-ab title="Противодействие терроризму и экстремизму">
    <h2 class="ab__subtitle" style="margin-top: 0px">Что такое несанкционированный митинг?</h2>
    <div class="ab__video">
      <video class="ab__video" controls>
        <source src="/video/Chto_takoe_nesanktsionirovanniy_miting.mp4" type="video/mp4" />
        Ваш браузер не поддерживает видео
      </video>
    </div>
    <h2 class="ab__subtitle" style="margin-top: 0px">Ответственность за экстремизм</h2>
    <div class="ab__video">
      <video class="ab__video" controls>
        <source src="/video/Otvetstvennosty_za_ekstremizm.mp4" type="video/mp4" />
        Ваш браузер не поддерживает видео
      </video>
    </div>
    <h2 class="ab__subtitle" style="margin-top: 0px">Правила поведения в социальных сетях</h2>
    <div class="ab__video">
      <video class="ab__video" controls>
        <source src="/video/Pravila_povedeniya_v_sotsialynih_setyah.mp4" type="video/mp4" />
        Ваш браузер не поддерживает видео
      </video>
    </div>
    <common-documents-list json-path="documents/terror.json" />
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
