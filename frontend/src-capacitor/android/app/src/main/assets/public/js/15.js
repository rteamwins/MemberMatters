(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([[15],{"4ab3":function(e,t,r){"use strict";r.r(t);var n=function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("q-page",{staticClass:"flex flex-center"},[e.spinner&&!e.error?r("q-spinner",{attrs:{color:"primary-btn",size:"3em"}}):e._e(),e.spinner?e._e():r("q-banner",{staticClass:"bg-positive text-white"},[e._v("\n    "+e._s(e.$t("logoutPage.logoutSuccess"))+"\n  ")]),e.error?r("q-banner",{staticClass:"bg-negative text-white"},[e._v("\n    "+e._s(e.$t("logoutPage.logoutFailed"))+"\n  ")]):e._e()],1)},o=[],s=(r("8e6e"),r("8a81"),r("ac6a"),r("cadf"),r("06db"),r("456d"),r("c47a")),a=r.n(s),c=r("bc3a"),i=r.n(c),u=r("2f62");function p(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,n)}return r}function l(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?p(Object(r),!0).forEach((function(t){a()(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):p(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}var g={name:"LogoutPage",data:function(){return{error:!1,spinner:!0}},mounted:function(){var e=this;i.a.post("/api/logout/").then((function(t){!0===t.data.success?e.completeLogout():e.error=!0})).catch((function(t){if(401!==t.response.status)throw e.error=!0,t;e.completeLogout()}))},methods:l({},Object(u["d"])("profile",["setLoggedIn","resetState"]),{completeLogout:function(){var e=this;this.resetState(),this.setLoggedIn(!1),this.error=!1,this.spinner=!1,setTimeout((function(){e.$router.push({name:"login"})}),2e3)}})},f=g,b=r("2877"),h=r("eebe"),O=r.n(h),d=r("9989"),m=r("0d59"),w=r("54e1"),j=Object(b["a"])(f,n,o,!1,null,null,null);t["default"]=j.exports;O()(j,"components",{QPage:d["a"],QSpinner:m["a"],QBanner:w["a"]})}}]);
//# sourceMappingURL=15.js.map