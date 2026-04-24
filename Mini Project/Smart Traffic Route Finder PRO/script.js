const graph = {
Home:{Market:2,School:4},
Market:{Home:2,Hospital:5,BusStand:3},
School:{Home:4},
Hospital:{Market:5,RailwayStation:6},
BusStand:{Market:3,RailwayStation:4},
RailwayStation:{Hospital:6,BusStand:4}
};

function sleep(ms){
return new Promise(resolve=>setTimeout(resolve,ms));
}

async function dijkstra(start,end){

let dist={},prev={},visited=[];

for(let node in graph) dist[node]=Infinity;
dist[start]=0;

while(true){

let closest=null;

for(let node in dist){
if(!visited.includes(node) &&
(closest===null || dist[node]<dist[closest])){
closest=node;
}
}

if(closest===null) break;
if(closest===end) break;

visited.push(closest);

document.getElementById(closest).classList.add("visited");
await sleep(700);

for(let neighbor in graph[closest]){
let newDist=dist[closest]+graph[closest][neighbor];

if(newDist<dist[neighbor]){
dist[neighbor]=newDist;
prev[neighbor]=closest;
}
}
}

let path=[];
let curr=end;

while(curr){
path.unshift(curr);
curr=prev[curr];
}

for(let node of path){
document.getElementById(node).classList.remove("visited");
document.getElementById(node).classList.add("path");
await sleep(700);
}

document.getElementById("result").innerHTML=
"Shortest Route: "+path.join(" ➜ ")+"<br>Total Distance: "+dist[end]+" km";
}

function resetGraph(){
document.querySelectorAll(".node").forEach(node=>{
node.classList.remove("visited","path");
});
document.getElementById("result").innerHTML="";
}

function startPath(){
resetGraph();

let source=document.getElementById("source").value;
let destination=document.getElementById("destination").value;

if(source===destination){
document.getElementById("result").innerHTML="Choose different nodes";
return;
}

dijkstra(source,destination);
}