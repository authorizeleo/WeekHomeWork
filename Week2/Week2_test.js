

{/* 第一題 */}
function calculate(min, max){
    s = 0
    for (let i=min ; i < max+1 ; i ++){
          s += i
          console.log(s)
    }
    console.log("計算結果", s)
}
calculate(1, 3); // 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8); // 你的程式要能夠計算 4+5+6+7+8，最後印出 30



 {/* 第二題 */}
function avg(data){
    let count = data.count
    let salary_data = data.employees
    let salary = 0;
    for (let i=0 ; i < count ; i++){
        salary += salary_data[i].salary
        // console.log(salary)
    }
    let avg_salary = parseInt(salary / count)

    console.log("每個員工平均薪資 "+ avg_salary + "元")

}

avg({
"count":3,
"employees":[
{
"name":"John",
"salary":30000
},
{
"name":"Bob",
"salary":60000
},
{
"name":"Jenny",
"salary":50000
}
]
});


// 第三題
function maxProduct(nums){
    let x = 0
    let a = []
    for (let i = 0; i < nums.length ; i++){ 
        for(let j = 1 ; j < nums.length ; j++){
            x = nums[i] * nums[j]
            if( i != j){
                a.push(x)
            }
        }     
       
    }
    console.log("相乘最大值: ",Math.max(...a))
   
    
}
maxProduct([5, 20, 2, 6]); // 得到 120 因為 20 和 6 相乘得到最大值
maxProduct([10, -20, 0, 3]); // 得到 30 因為 10 和 3 相乘得到最大值
maxProduct([-10, -20, 5, 2, 1]) 



            // 第四題
function twoSum(nums, target){
    let a = 0
    for(let i = 0 ; i < nums.length ; i++){
        for(let j = 1 ; i < nums.length ; j++ ){
             if ( nums[i] + nums[j] === target){
                 return [i,j]
             } 
        }
    }
    
    
    
// your code here
}
result=twoSum([2, 11, 7, 15], 9)
console.log(result) // show [0, 2] because nums[0]+nums[2] is 9

function maxZeros(nums){
    let x = 0
    let y = []
    for (let z= 0 ; z < nums.length ; z++){
        if (nums[z] == 0){
            x += 1 
            y.push(x)
        }else if(nums[z] == 1){
            x = 0
            y.push(x)
        } 
    }
    console.log(Math.max(...y))
// 請用你的程式補完這個函式的區塊
}
maxZeros([0, 1, 0, 0]) // 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) // 得到 4
maxZeros([1, 1, 1, 1, 1]) // 得到 0


