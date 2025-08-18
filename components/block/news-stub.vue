<template>
  <a href="https://vk.com/omsktec" class="stub">
    <h1 class="stub__title">Актуальные новости доступны в группе VK</h1>
    <icon-wrapper width="192" height="192" class="stub__icon">
      <IconVK />
    </icon-wrapper>
    <div class="stub__circle" />
  </a>
</template>

<script>
export default {
  name: 'BlockNewsStub',
}
</script>

<style scoped lang="scss">
.stub {
  background: #fdfdfd;
  border: 1px solid #c7c7c7;
  box-sizing: border-box;
  box-shadow: 0px 20px 90px 7px rgba(0, 0, 0, 0.08);
  border-radius: 16px;
  padding: 50px 24px 32px 24px;
  display: block;
  transition: $t border-color;
  &__title {
    font-family: Montserrat;
    font-style: normal;
    font-weight: 600;
    font-size: 24px;
    line-height: 28px;
    display: flex;
    align-items: center;
    justify-content: center;
    max-width: 350px;
    text-align: center;
  }
  &__icon {
    margin: 0 auto;
    color: #c56464;
  }
  &__circle {
    position: absolute;
    right: 12px;
    top: 12px;
    width: 32px;
    height: 32px;
    background-color: #c56464;
    border-radius: 50%;
  }
  @include medium-media {
    padding: 12px;
    &__title {
      font-size: 16px;
      line-height: 18px;
    }
    &__icon {
      min-width: 100px !important;
      min-height: 100px !important;
      height: 100px !important;
      width: 100px !important;
    }
    &__circle {
      width: 12px;
      height: 12px;
      top: 6px;
      right: 6px;
    }
  }
  &:hover {
    border-color: rgba($accent-color, 0.5);
  }
}
</style>
