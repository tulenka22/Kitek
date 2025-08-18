<template>
  <div class="contacts">
    <AppBlock
      title="Местоположение корпусов"
      :content-style="{ padding: 0 }"
      :block-style="{ padding: 0 }"
    >
      <div class="contacts__map">
        <client-only>
          <l-map :zoom="16" :center="[55.02653842901682, 73.3838069868169]">
            <l-tile-layer
              url="http://{s}.tile.osm.org/{z}/{x}/{y}.png"
            ></l-tile-layer>
            <l-marker :lat-lng="[55.02653842901682, 73.3838069868169]">
              <l-tooltip content="Административный корпус" />
            </l-marker>
            <l-marker :lat-lng="[55.02384074021159, 73.38373106957242]">
              <l-tooltip content="Корпус №1" />
            </l-marker>
            <l-marker :lat-lng="[55.023744176785854, 73.38217582481475]">
              <l-tooltip content="Корпус №2" />
            </l-marker>
            <l-marker :lat-lng="[55.009811737433665, 73.33504684810141]">
              <l-tooltip content="Корпус №3" />
            </l-marker>
          </l-map>
        </client-only>
      </div>
    </AppBlock>
  </div>
</template>

<script>
export default {
  name: 'BlockMap',
}
</script>

<style scoped lang="scss">
.contacts {
  margin-top: 60px;
  &__map {
    width: 100%;
    height: 500px;
    border-radius: 5px;
    overflow: hidden;
    @include medium-media {
      height: 350px;
    }
  }
}
</style>
