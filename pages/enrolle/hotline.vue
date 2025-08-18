<template>
  <block-ab title="Горячая линия в системе СПО">
    <img src="/img/news/hotline.jpg" />
    <button class="back" @click="$router.go(-1)">Назад</button>
  </block-ab>
</template>

<script>
export default {}
</script>

<style scoped lang="scss">
img {
  margin: 20px;
  padding: 0;
}
.back {
  position: absolute;
  right: 16px;
  top: -50px;
  color: $bg-primary;
  background-color: $accent-color;
  padding: 12px 24px;
  border-radius: 12px;
  @include medium-media {
    position: fixed;
    top: 85px;
    right: 15px;
  }
}
</style>
