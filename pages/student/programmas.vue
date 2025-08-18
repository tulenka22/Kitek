<template>
  <block-ab title="ПРОГРАММА ДОЛГОСРОЧНЫХ СБЕРЕЖЕНИЙ">
    <div class="img-container">
      <img class="img-single__minimg" src="/img/events/Плакат_А2_1_печать.webp" />
    </div>
    <common-documents-list json-path="documents/programms.json" />
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
