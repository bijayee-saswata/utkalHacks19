Vue.filter("formatDate", function(value) {
  if (value) {
    return moment(String(value)).format("MM/DD/YYYY hh:mm");
  }
});
var app = new Vue({
  el: "#app",
  delimiters: ["[[", "]]"],
  data: {
    date: "",
    items: [
      {
        date: "",
        name: "name1",
        email: "strfd@gfg.co",
        location: "bbsr",
        amount: "20000"
      },
      { date: "", name: "", email: "", location: "", amount: "" },
      { date: "", name: "", email: "", location: "", amount: "" }
    ]
  },
  methods: {
    randomNumber: function() {
      return "Trd" + Math.floor(Math.random() * 100000);
    },
    showResult() {
      alert("hello");
    }
  },
  created() {
    this.date = Date.now();
  }
  //   computed: {
  //     formatted() {
  //       return Vue.filter("date")(this.value);
  //     }
  //   }
});
