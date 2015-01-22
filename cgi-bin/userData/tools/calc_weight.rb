# coding: utf-8

# LIBSVMのモデルファイルを解析するスクリプト
# 素性とその重みを出力する (ソートはされていない)
# 使い方: ruby calc_weight.rb < [モデルファイル]

weight = Hash.new

# パラメータを読み飛ばす
8.times do
  STDIN.gets
end

# モデルファイルの解析
while line = STDIN.gets
  line = line.split(" ")

  # coefficientを取得
  coe = line[0].to_f
  line.shift

  # svを取得
  sv = Hash.new
  line.each do |element|
    sv[element.split(":")[0].to_i] = ((element.split(":")[1]).chomp).to_f
  end

  sv.each_key do |key|
    if weight[key]
      weight[key] += coe * sv[key]
    else
      weight[key] = coe * sv[key]
    end
  end
end

# 重みの出力
weight.each_key do |key|
  puts key.to_s + ' ' +weight[key].to_s
end
