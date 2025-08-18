<template>
  <block-ab title="ПАО ''Россети Сибири''">
    <h2 class="ab__subtitle" style="margin-top: 0px">
      "Омскэнерго" в целях сохранения жизни и здоровья обучающихся образовательных организаций
      Омской области проводит информационно-разъяснительную работу. Представленный ПАО видеоролик
      популярно разъясняет студентам о последствиях электротравм и правилах безопасного поведения
      вблизи энергообъектов. По рекомендации Министерства образования Омской области в целях
      профилактики электротравматизма данный материал был представлен студентам, а так же размещен в
      родительских чатах.
    </h2>
    <div class="ab__video">
      <video class="ab__video" controls>
        <source src="/video/Электробезопасность ТП Россети Сибирь.mp4" type="video/mp4" />
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
