import{s as r,t as c,o as f,c as h,w as l,v as m,i as d,a as t,x as i,y as p,h as M,z as O}from"./index-58f9f511.js";import{_ as b}from"./_plugin-vue_export-helper-c27b6911.js";const n=r(),{setting:a}=c(n),V={data(){return{banMode:"Off",shillMode:"Off"}},created(){a.value===null?n.fetch().then(()=>{this.banMode=a.value.ban_mode?"On":"Off",this.shillMode=a.value.shill_mode?"On":"Off"}):(this.banMode=a.value.ban_mode?"On":"Off",this.shillMode=a.value.shill_mode?"On":"Off")},methods:{async update(){await n.update(this.banMode,this.shillMode)}}};function v(_,s,S,x,e,u){return f(),h(m,{width:"400"},{title:l(()=>[d(" Shillmaster Bot Default Setting ")]),text:l(()=>[t(i,{modelValue:e.shillMode,"onUpdate:modelValue":s[0]||(s[0]=o=>e.shillMode=o),"hide-details":"","true-value":"On",color:"success","false-value":"Off",label:`Shill Mode Turned ${e.shillMode}`},null,8,["modelValue","label"]),t(i,{modelValue:e.banMode,"onUpdate:modelValue":s[1]||(s[1]=o=>e.banMode=o),"hide-details":"","true-value":"On",color:"success","false-value":"Off",label:`Ban Mode Turned ${e.banMode}`},null,8,["modelValue","label"])]),default:l(()=>[t(O,null,{default:l(()=>[t(p),t(M,{variant:"tonal","prepend-icon":"mdi-check-circle",class:"px-5",color:"success",onClick:u.update},{default:l(()=>[d("Save")]),_:1},8,["onClick"])]),_:1})]),_:1})}const w=b(V,[["render",v]]);export{w as default};
