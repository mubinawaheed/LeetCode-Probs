/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    let a=[]
    arr.forEach((e,i)=>{
        if (fn(e,i)){
            a.push(e)
        }
    })
    return a
};