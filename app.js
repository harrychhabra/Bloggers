/**
 * @Author: shadabKhan
 * @Date:   Thursday, November 7th 2019, 5:44:38 pm
 * @Last modified by:   shadabKhan
 * @Last modified time: Thursday, November 7th 2019, 7:38:06 pm
 */

const b = document.getElementById('btn');
b.addEventListener("click", () => {document.getElementById('h1').innerHTML = "changed";} );

function temp() {
  // console.log("ada");
  document.getElementById("h1").innerHTML = "changed";
}
