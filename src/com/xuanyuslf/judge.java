package com.xuanyuslf;

import java.util.*;

public class judge {
    public static int len = (Main.base.size() / 3)-1;
    //数据类型对除法有影响,若为整形,则除法取整
    public static int f = -1;
    public static List<String> aminoAcid=new ArrayList<>();
    public static void judge1(){
        for(int i=0;i < len-f;i++){
            if(Objects.equals(Main.base.get(0), "U")){
                if (Objects.equals(Main.base.get(1), "U")){
                    if (Objects.equals(Main.base.get(2), "U")){
                        judge.remove();
                        aminoAcid.add("苯丙氨酸");
                    }
                    else if (Objects.equals(Main.base.get(2), "C")){
                        judge.remove();
                        aminoAcid.add("苯丙氨酸");
                    }
                    else if (Objects.equals(Main.base.get(2), "A")){
                        judge.remove();
                        aminoAcid.add("亮氨酸");
                    }
                    else if (Objects.equals(Main.base.get(2), "G")){
                        judge.remove();
                        aminoAcid.add("亮氨酸");
                    }
                }
                else if (Objects.equals(Main.base.get(1), "C")){
                    judge.remove();
                    aminoAcid.add("丝氨酸");
                }
                else if (Objects.equals(Main.base.get(1), "A")){
                    if (Objects.equals(Main.base.get(2), "U")){
                        judge.remove();
                        aminoAcid.add("络氨酸");
                    }
                    else if (Objects.equals(Main.base.get(2), "C")){
                        judge.remove();
                        aminoAcid.add("酪氨酸");
                    }
                    else {
                        break;
                    }
                }
                else if (Objects.equals(Main.base.get(1), "G")){
                    if (Objects.equals(Main.base.get(2), "U")){
                        judge.remove();
                        aminoAcid.add("半胱氨酸");
                    }
                    else if (Objects.equals(Main.base.get(2), "C")){
                        judge.remove();
                        aminoAcid.add("半胱氨酸");
                    }
                    else if (Objects.equals(Main.base.get(2), "G")){
                        judge.remove();
                        aminoAcid.add("色氨酸");
                    }
                    else {
                        break;
                    }
                }
            }
            else if (Objects.equals(Main.base.get(0), "C")){
                if (Objects.equals(Main.base.get(1), "U")){
                    judge.remove();
                    aminoAcid.add("亮氨酸");
                }
                else if (Objects.equals(Main.base.get(1), "C")){
                    judge.remove();
                    aminoAcid.add("脯氨酸");
                }
                else if (Objects.equals(Main.base.get(1), "A")){
                    if (Objects.equals(Main.base.get(2), "U")){
                        judge.remove();
                        aminoAcid.add("组氨酸");
                    }
                    else if (Objects.equals(Main.base.get(2), "C")){
                        judge.remove();
                        aminoAcid.add("组氨酸");
                    }
                    else {
                        judge.remove();
                        aminoAcid.add("谷氨酰酸");
                    }
                }
                else if (Objects.equals(Main.base.get(1), "G")){
                    judge.remove();
                    aminoAcid.add("精氨酸");
                }
            }
            else if (Objects.equals(Main.base.get(0), "A")){
                if (Objects.equals(Main.base.get(1), "U")){
                    if (Objects.equals(Main.base.get(2), "G")){
                        judge.remove();
                        aminoAcid.add("甲硫氨酸");
                    }
                    else {
                        judge.remove();
                        aminoAcid.add("异亮氨酸");
                    }
                }
                else if (Objects.equals(Main.base.get(1), "C")){
                    judge.remove();
                    aminoAcid.add("苏氨酸");
                }
                else if (Objects.equals(Main.base.get(1), "A")){
                    if (Objects.equals(Main.base.get(2), "U")){
                        judge.remove();
                        aminoAcid.add("天冬氨酸");
                    }
                    else if (Objects.equals(Main.base.get(2), "C")){
                        judge.remove();
                        aminoAcid.add("天冬氨酸");
                    }
                    else if (Objects.equals(Main.base.get(2), "A")){
                        judge.remove();
                        aminoAcid.add("赖氨酸");
                    }
                    else if (Objects.equals(Main.base.get(2), "G")){
                        judge.remove();
                        aminoAcid.add("赖氨酸");
                    }
                }
                else if (Objects.equals(Main.base.get(1), "G")){
                    if (Objects.equals(Main.base.get(2), "U")){
                        aminoAcid.add("丝氨酸");
                    }
                    else if (Objects.equals(Main.base.get(2), "C")){
                        judge.remove();
                        aminoAcid.add("丝氨酸");
                    }
                    else if (Objects.equals(Main.base.get(2), "A")){
                        judge.remove();
                        aminoAcid.add("精氨酸");
                    }
                    else if (Objects.equals(Main.base.get(2), "G")){
                        judge.remove();
                        aminoAcid.add("精氨酸");
                    }
                }
            }
            else if (Objects.equals(Main.base.get(0), "G")){
                if (Objects.equals(Main.base.get(1), "U")){
                    judge.remove();
                    aminoAcid.add("缬氨酸");
                }
                else if (Objects.equals(Main.base.get(1), "C")){
                    judge.remove();
                    aminoAcid.add("丙氨酸");
                }
                else if (Objects.equals(Main.base.get(1), "A")){
                    if (Objects.equals(Main.base.get(2), "U")){
                        judge.remove();
                        aminoAcid.add("天冬氨酸");
                    }
                    else if (Objects.equals(Main.base.get(2), "C")){
                        judge.remove();
                        aminoAcid.add("天冬氨酸");
                    }
                    else {
                        judge.remove();
                        aminoAcid.add("谷氨酸");
                    }
                }else if (Objects.equals(Main.base.get(1), "G")){
                    judge.remove();
                    aminoAcid.add("甘氨酸");
                }
            }
        }
    }
    public static void judge2(){
        String[] a = {"A","G","C","U"};
        List<String> list1 = Arrays.asList(a);
        if (!(list1.containsAll(Main.base))){
            System.out.println("碱基有误");
            System.exit(0);
        }
    }
    public static void judge3(){
        List<String> base1 = new ArrayList<>();
        String [] judge1 = {"A","U","G"};
        String [] judge2 = {"G","U","G"};
        List<String> judgeList1 = Arrays.asList(judge1);
        List<String> judgeList2 = Arrays.asList(judge2);
        for (int i = 0 ;i<Main.a.length(); i++){
            f = f + 1;
            base1.add(Main.base.get(0));
            base1.add(Main.base.get(1));
            base1.add(Main.base.get(2));
            if (base1.equals(judgeList1)){
                aminoAcid.add("甲硫氨酸");
                judge.remove();
                break;
            }
            else if (base1.equals(judgeList2)){
                aminoAcid.add("缬氨酸");
                judge.remove();
                break;
            }
            else {
                if (f == len){
                    System.out.println("无法形成氨基酸");
                    System.exit(0);
                }
                else {
                    judge.remove();
                    base1.clear();
                }
            }
        }

    }
    public static void remove(){
        Main.base.remove(0);
        Main.base.remove(0);
        Main.base.remove(0);
    }
}