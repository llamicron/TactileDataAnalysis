var app = new Vue({
  el: '#main',
  data: {
    time: 5,
    skip: 5,
    skippers: []
  },

  methods: {
    refreshDataSet() {
      axios.post('/refresh-data-set', {
        time: this.time,
        skip: this.skip
      }).then(response => {
        this.skippers = response.data;
        console.log(response);
      }).catch(error => {
        console.log(error);
      })
    }
  },

  mounted() {
    this.refreshDataSet();
  },

  computed: {
    guids() {
      guids = []
      this.skippers.forEach(skipper => {
        guids.push(skipper.guid)
      });
      return guids
    },
    shortGuids() {
      guids = []
      this.skippers.forEach(skipper => {
        guids.push(skipper.guid.slice(24, 36))
      });
      return guids
    },
  },

  watch: {
    time() {
      this.refreshDataSet();
    },
    skip() {
      this.refreshDataSet();
    }
  }
})
