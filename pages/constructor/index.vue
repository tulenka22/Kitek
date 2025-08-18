<template>
  <block-ab title="Конструктор событий">
    <div class="form">
      <div class="events-holder">
        <entities-event-card
          @click.native.stop.prevent="selectCard(event)"
          v-for="(event, eventIdx) of events"
          :key="eventIdx"
          :instance="event" />
      </div>

      <div class="form__inputs">
        <common-input class="form__control" v-model="selectedOrNewEvent.title" label="Заголовок" />
        <common-input
          class="form__control"
          v-model="selectedOrNewEvent.subtitle"
          label="Подзаголовок" />
        <common-input
          class="form__control"
          v-model="selectedOrNewEvent.link"
          label="Ссылка"
          value="#" />
        <div class="form__group" v-if="!isSelected">
          <common-button class="form__control form__control-button" @click="addNew">
            Добавить
          </common-button>
          <div class="form__divider" />
          <common-button class="form__control form__control-button" @click="cleanFields">
            Очистить поля
          </common-button>
        </div>
        <template v-else>
          <div class="form__group">
            <common-button class="form__control form__control-button" @click="deleteEvent">
              Удалить
            </common-button>
            <div class="form__divider" />
            <common-button class="form__control form__control-button" @click="saveEvent">
              Сохранить
            </common-button>
          </div>
          <common-button class="form__control form__control-button" @click="createNew">
            Добавить новое событие
          </common-button>
        </template>

        <div class="form__info">
          <h2><b>Как пользоваться конструктором?</b></h2>
          <p>Для редактирования нажмите на любую из карточек слева</p>
          <h2><b>Что делать после добавления новых событий?</b></h2>
          <p>Нажмите на 'скопировать код' и вставте его в events.json</p>
        </div>
      </div>
      <div class="events-holder events-holder-preview">
        <h2 class="events-holder__title">Предпросмотр</h2>
        <entities-event-card :instance="selectedOrNewEvent" />
      </div>
    </div>
    <common-button class="copy-button" @click="copyCode"> Скопировать код </common-button>
  </block-ab>
</template>

<script>
// Todo: Save as file
import { loadDynamic } from '~/core/helpers/file'
export default {
  async created() {
    try {
      this.events = JSON.parse(await loadDynamic('dynamic/news/events.json'))
    } catch {
      console.log('Проверьте валидность JSON новостей и событий!')
    }
  },
  data() {
    return {
      events: [],
      selectedOrNewEvent: {
        id: 1337,
        title: 'Заголовок',
        subtitle: 'Подзаголовок',
        link: '#',
      },
    }
  },
  computed: {
    isSelected() {
      return this.events.some((e) => this.selectedOrNewEvent.id === e.id)
    },
  },
  methods: {
    copyCode() {
      navigator.clipboard.writeText(JSON.stringify(this.events))
    },
    selectCard(event) {
      this.selectedOrNewEvent = { ...event }
    },
    createNew() {
      this.selectedOrNewEvent = {
        id: Date.now(),
        title: 'Заголовок',
        subtitle: 'Подзаголовок',
        link: '#',
      }
    },
    deleteEvent() {
      this.events = this.events.filter((e) => e.id !== this.selectedOrNewEvent.id)
    },
    saveEvent() {
      const index = this.events.findIndex((e) => e.id === this.selectedOrNewEvent.id)
      this.$set(this.events, index, { ...this.selectedOrNewEvent })
    },
    cleanFields() {
      this.selectedOrNewEvent = {
        id: Date.now(),
        title: '',
        subtitle: '',
        link: '',
      }
    },
    addNew() {
      this.events.push(this.selectedOrNewEvent)
    },
  },
}
</script>

<style scoped lang="scss">
.form {
  display: flex;
  &__inputs {
    max-width: 500px;
    width: 100%;
  }
  &__control {
    margin-top: 6px;
    width: 100%;

    &-button {
      white-space: nowrap !important;
      padding: 12px !important;
      font-size: 16px !important;
      font-weight: 500 !important;
    }
  }
  &__info {
    margin-top: 60px;
    > p,
    > h2 {
      margin-top: 4px;
    }
    > h2 {
      margin-top: 12px;
    }
  }
  &__group {
    display: flex;
    align-items: center;
  }
  &__divider {
    display: block;
    width: 16px;
    flex: none;
  }
}
.events-holder {
  display: flex;
  flex-direction: column;
  gap: 4px;
  max-width: 350px;
  min-width: 350px;
  max-height: 600px;
  overflow: auto;
  @include scrollbar;
  margin-right: 32px;
  padding: 4px;
  &__title {
    font-size: 18px;
    font-weight: 600;
    margin-bottom: 12px;
    color: $accent-color;
  }
  &::v-deep .card {
    box-shadow: none;
    &:hover {
      box-shadow: none;
    }
  }
  &-preview {
    margin-right: 0;
    margin-left: 32px;
  }
}
.copy-button {
  margin-top: 12px;
  max-width: 350px;
  width: 100%;
}
</style>
