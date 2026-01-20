<template>
  <AppBlock
    :content-style="{
      padding: '24px',
    }"
    class="events__self testgipn"
    title="2025 ГОД ЗАЩИТНИКА ОТЕЧЕСТВА">
    <div class="left">
      <swiper :options="swiperOptions">
        <swiper-slide
          ><a href="https://omsktec.ru/enrolle/enrolle-menu"
            ><img
              style="width: auto; height: auto"
              class="event__img-main"
              alt="Events-Image"
              loading="preload"
              src="/img/organization/Bannerpobeda.webp" /> </a
        ></swiper-slide>
      </swiper>
    </div>
  </AppBlock>
</template>

<script>
export default {
  name: 'BannerMain',
}
</script>

<style scoped lang="scss">
.events__self {
  margin-bottom: 20px;
}
</style>
