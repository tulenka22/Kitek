<template>
  <block-ab title="ВСЕРОССИЙСКАЯ ЯРМАРКА ТРУДОУСТРОЙСТВО">
    <div class="img-container">
      <img class="img-single__minimg" src="/img/events/Всеросийская ярморка.webp" />
    </div>
    <div class="ab__video">
      <video class="ab__video" controls>
        <source src="/video/Ярмарка трудоустройства v2.mp4" type="video/mp4" />
        Ваш браузер не поддерживает видео
      </video>
    </div>
  </block-ab>
</template>

<script>
export default {}
</script>

<style scoped lang="scss">
.ab {
  &__video {
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
