/*
 * version : 6.5.3.12461
 * resolution : 1080*1920
 * description :
 */
define("version", "6.5.3.12461");
define("resolution", "1080*1920");
define("requireVersion", "1.7.0.12146");
var device = Device.searchObject(sigmaConst.DevSelectOne);

function run(length){
print("length= "+length +" px");
var num=0;
device.click(786, 541, sigmaConst.STATE_DOWN); 
var jump=(length+7)*(2.72);
print("jump="+jump);
device.delay(jump); 
device.click(786, 541, sigmaConst.STATE_UP); 
}

run(1);

