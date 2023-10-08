function hello(a,b){
    console.debug("Hello from Hello");
    this.a=a;
    this.b=b;
    this.saberi=function(){
        return this.a+this.b
    }
}