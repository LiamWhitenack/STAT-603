

##### (a)

![Steps](image.png)
![Smooth](image-1.png)

##### (b)


\[
F(t) =
\begin{cases}
0, & t < 1 \\
\frac{1}{8}, & 1 \leq t < 3 \\
\frac{3}{8}, & 3 \leq t < 5 \\
\frac{7}{8}, & 5 \leq t < 7 \\
1, & t \geq 7
\end{cases}
\]

\[
P(T = t) = F(t) - \lim\_{x \to t^-} F(x)
\]

- **At \( T = 1 \):**
  \[
  P(T = 1) = F(1) - F(0) = \frac{1}{8} - 0 = \frac{1}{8}
  \]

- **At \( T = 3 \):**
  \[
  P(T = 3) = F(3) - F(2) = \frac{3}{8} - \frac{1}{8} = \frac{2}{8} = \frac{1}{4}
  \]

- **At \( T = 5 \):**
  \[
  P(T = 5) = F(5) - F(4) = \frac{7}{8} - \frac{3}{8} = \frac{4}{8} = \frac{1}{2}
  \]

- **At \( T = 7 \):**
  \[
  P(T = 7) = F(7) - F(6) = 1 - \frac{7}{8} = \frac{1}{8}
  \]

| T   | P(T) |
| --- | ---- |
| 1   | 1/8  |
| 3   | 1/4  |
| 5   | 1/2  |
| 7   | 1/8  |

##### (c)


\[
P(1.4 < T < 6) = F(6) - F(1.4)
\]


\[
F(6) \text{ falls in the range } 5 \leq t < 7, \text{ where } F(5) = \frac{7}{8}.
\]

\[
F(6) = F(5) = \frac{7}{8}
\]


\[
F(1.4) \text{ falls in the range } 1 \leq t < 3, \text{ where } F(1) = \frac{1}{8}.
\]


\[
F(1.4) = F(1) = \frac{1}{8}
\]


\[
P(1.4 < T < 6) = F(6) - F(1.4)
\]

\[
= \frac{7}{8} - \frac{1}{8} = \frac{6}{8} = \frac{3}{4}
\]

\[
P(1.4 < T < 6) = \frac{3}{4}
\]


##### (d)


\[
P(A \mid B) = \frac{P(A \cap B)}{P(B)}
\]


- \( A = \{T \leq 5\} \)
- \( B = \{T \geq 2\} \)


\[
P(T \leq 5 \mid T \geq 2) = \frac{P(2 \leq T \leq 5)}{P(T \geq 2)}
\]

\[
P(T \geq 2) = 1 - P(T < 2)
\]


\[
P(T < 2) = F(2) = F(1) = \frac{1}{8}
\]


\[
P(T \geq 2) = 1 - \frac{1}{8} = \frac{7}{8}
\]

\[
P(2 \leq T \leq 5) = P(T = 3) + P(T = 5)
\]


\[
P(T = 3) = \frac{1}{4}, \quad P(T = 5) = \frac{1}{2}
\]

\[
P(2 \leq T \leq 5) = \frac{1}{4} + \frac{1}{2} = \frac{3}{4}
\]

\[
P(T \leq 5 \mid T \geq 2) = \frac{P(2 \leq T \leq 5)}{P(T \geq 2)}
\]

\[
= \frac{\frac{3}{4}}{\frac{7}{8}}
\]

\[
= \frac{3}{4} \times \frac{8}{7} = \frac{24}{28} = \frac{6}{7}
\]

\[
P(T \leq 5 \mid T \geq 2) = \frac{6}{7}
\]

