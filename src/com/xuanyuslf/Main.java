package com.xuanyuslf;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static List<String> base = new ArrayList<>();
    public static String a;
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        System.out.print("请输入mRNA上的碱基(注:头为起始的碱基):");
        a = s.next();
        for(int i=0;i < a.length();i++){
            base.add(String.valueOf(a.charAt(i)));
            //将基本数据型态转换成String的static方法——String.valueOf()
        }
        judge.judge2();
        judge.judge3();
        judge.judge1();
        System.out.println(judge.aminoAcid);
    }
}