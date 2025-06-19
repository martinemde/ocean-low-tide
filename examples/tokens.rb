#!/usr/bin/env ruby
# frozen_string_literal: true

# Comments and documentation
=begin
Multi-line comment block
for testing theme colors
=end

require 'json'
require 'net/http'
require_relative 'other_file'

# Constants and variables
CONSTANT_VALUE = 42
@@class_variable = "class variable"
@instance_variable = "instance variable"
$global_variable = "global variable"
local_variable = "local variable"

# Numbers and literals
integer = 123
float = 3.14159
binary = 0b1010
octal = 0o777
hex = 0xFF
scientific = 1.23e-4
negative = -456

# Strings and interpolation
single_quoted = 'single quoted string'
double_quoted = "double quoted with #{interpolation}"
heredoc = <<~HEREDOC
  This is a heredoc
  with multiple lines
HEREDOC

raw_string = %q{raw string with 'quotes'}
interpolated_string = %Q{interpolated #{raw_string}}
word_array = %w[word array elements]
symbol_array = %i[symbol array elements]

# Regular expressions
regex1 = /pattern/i
regex2 = %r{pattern with #{interpolation}}mix
regex3 = /\d+\.\d+/

# Symbols
symbol = :symbol_name
dynamic_symbol = :"dynamic_#{symbol}"

# Arrays and hashes
array = [1, 2, 3, "mixed", :types]
hash = {
  key: "value",
  "string_key" => 42,
  :symbol_key => true,
  nested: { inner: "hash" }
}

# Ranges
inclusive_range = 1..10
exclusive_range = 1...10

# Class definition
# @api public
class ExampleClass < StandardError
  include Enumerable
  extend Forwardable
  include Module::ExampleModule

  attr_reader :readonly
  attr_writer :writeonly
  attr_accessor :readwrite

  CONSTANT = "constant"

  # Lot's more documentation
  # Here we go, this is great documentation
  # @param param [String] The parameter for the class
  # @param keyword [String] The keyword parameter for the class
  # @return [String] The return value of the class
  # @raise [StandardError] The error raised by the class
  def initialize(param = "default", keyword: "default")
    @instance_variable = param
    @@class_variable += " modified"
    constant = CONSTANT
    klass = ExampleClass
    instance_method(
    super()
  end

  def self.class_method
    "This is a class method"
  end

  def instance_method(required, optional = nil, *splat, **kwargs, &block)
    yield if block_given?
    self
    [required, optional, splat, kwargs]
  end

  def each
    (1..3).each { |i| yield i }
  end

  private

  def private_method
    "private"
  end

  protected

  def protected_method
    "protected"
  end
end

# Module definition
module ExampleModule
  def self.included(base)
    base.extend(ClassMethods)
  end

  def module_method
    "module instance method"
  end

  module ClassMethods
    def extended_method
      "extended class method"
    end
  end
end

# Struct and lambda
Person = Struct.new(:name, :age) do
  def adult?
    age >= 18
  end
end

# Procs and lambdas
proc_example = proc { |x| x * 2 }
lambda_example = lambda { |x| x * 2 }
stabby_lambda = ->(x) { x * 2 }

# Control flow
if true
  puts "if statement"
elsif false
  puts "elsif"
else
  puts "else"
end

case "value"
when "value"
  puts "matched"
when /\\\A(?:test)\)\[[^uehtnous]?{1,3}<$%!^.*pat#{self}\z/
  puts "regex match"
else
  puts "default"
end

# Loops
while false
  break
end

until true
  next
end

for i in 1..3
  redo if i == 2
end

# Iterators and blocks
[1, 2, 3].each do |item|
  puts item
end

{a: 1, b: 2}.each_pair { |k, v| puts "#{k}: #{v}" }

# Exception handling
begin
  raise StandardError, "error message"
rescue StandardError => e
  puts e.message
rescue => e
  puts "caught: #{e}"
ensure
  puts "cleanup"
end

# Method definitions with various syntaxes
def method_with_defaults(a, b = 10, c: 20, d: nil, **opts, &block)
  return a + b unless block_given?
  yield(a, b)
end

# Singleton method
def ExampleClass.singleton_method
  "singleton"
end

# Operator overloading
class Point
  def initialize(x, y)
    @x, @y = x, y
  end

  def +(other)
    Point.new(@x + other.x, @y + other.y)
  end

  def ==(other)
    @x == other.x && @y == other.y
  end

  def [](index)
    index == 0 ? @x : @y
  end

  def []=(index, value)
    index == 0 ? @x = value : @y = value
  end

  protected

  attr_reader :x, :y
end

# Metaprogramming
class Dynamic
  define_method(:dynamic_method) do |arg|
    "Dynamic method called with #{arg}"
  end

  def method_missing(method_name, *args, &block)
    if method_name.to_s.start_with?('find_by_')
      attribute = method_name.to_s.sub('find_by_', '')
      "Finding by #{attribute} with #{args.first}"
    else
      super
    end
  end

  def respond_to_missing?(method_name, include_private = false)
    method_name.to_s.start_with?('find_by_') || super
  end
end

# String methods and chaining
result = "hello world"
  .upcase
  .gsub(/WORLD/, 'RUBY')
  .split
  .map(&:downcase)
  .join('-')

# Numeric methods
42.times { |i| puts i if i.even? }
(1..10).select(&:odd?).map { |n| n ** 2 }

# File operations
File.open('example.txt', 'w') do |file|
  file.puts "Writing to file"
end if false

# Constants and namespacing
module Namespace
  CONSTANT = "namespaced constant"

  class NestedClass
    def self.method
      CONSTANT
    end
  end
end

# Refinements
module StringRefinements
  refine String do
    def palindrome?
      self == reverse
    end
  end
end

# Using refinements
using StringRefinements

# Keyword arguments
def keyword_method(required:, optional: "default", **rest)
  { required: required, optional: optional, rest: rest }
end

# Pattern matching (Ruby 3.0+)
case [1, 2, 3]
in [1, 2, 3]
  puts "exact match"
in [1, *rest]
  puts "starts with 1, rest: #{rest}"
else
  puts "no match"
end

# Endless method definitions (Ruby 3.0+)
def add(a, b) = a + b

# Multiple assignment
a, b, *rest = [1, 2, 3, 4, 5]
x, y = y, x if defined?(y)

# Conditional assignment
value ||= "default value"
hash[:key] &&= "modified"

# Safe navigation
object&.method&.chain

# Frozen string literal
"frozen string".freeze

# Special variables
puts "Script name: #{$0}"
puts "Process ID: #{$$}"
puts "Last match: #{$&}" if "test" =~ /es/

# Encoding
# encoding: utf-8
"unicode: 🚀 ñ ü"

# Data and __END__
puts DATA.read if defined?(DATA)

__END__
This is data after __END__
It can be read using DATA constant
