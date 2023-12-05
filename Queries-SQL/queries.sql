-- Checando os dados. Há duplicados? se sim, quantas linhas duplicadas?
SELECT
    COUNT(*) AS total_duplicatas
FROM
    (
    SELECT
        price,
        condo,
        size,
        rooms,
        toilets,
        suites,
        parking,
        elevator,
        furnished,
        swimming_pool,
        new, district,
        negotiation_type,
        property_type,
        latitude,
        longitude,
        COUNT(*) AS count_duplicatas
    FROM
        raw
    GROUP BY
        price, condo, size, rooms, toilets, suites, parking, elevator, furnished, swimming_pool, new, district,
        negotiation_type, property_type, latitude, longitude
    HAVING
        COUNT(*) > 1
    ) AS duplicatas;


-- Calculando a média de preços (em cima da base sem dados duplicados), considerando o tipo de negociação: Aluguel ou Venda
SELECT
    negotiation_type,
    ROUND(AVG(price), 2) AS avg_price,
    COUNT(*) AS count_properties
FROM
    (SELECT DISTINCT * FROM raw)
GROUP BY negotiation_type;


-- Cálculo da média do preço de aluguel e venda, por distrito
SELECT
    district,
    AVG(CASE WHEN negotiation_type = 'rent' THEN price END) AS avg_rent_price,
    AVG(CASE WHEN negotiation_type = 'sale' THEN price END) AS avg_sale_price
FROM
    raw
GROUP BY
    district
ORDER BY
    district;


-- Contagem de imóveis com/sem elevador e com/sem piscina, para aluguel e venda
SELECT
    negotiation_type,
    elevator,
    swimming_pool,
    COUNT(*) AS count_properties
FROM
    raw
GROUP BY
    negotiation_type, elevator, swimming_pool
ORDER BY negotiation_type;


-- Distribuição de tipos de propriedades para aluguel e venda:
SELECT
    negotiation_type,
    property_type,
    COUNT(*) AS count_properties
FROM
    raw
GROUP BY
    negotiation_type, property_type;


-- Média do tamanho dos imóveis, por tipo de propriedade, para aluguel e venda:
SELECT
    negotiation_type,
    property_type,
    ROUND(AVG(size), 2) AS avg_size
FROM
    raw
GROUP BY
    negotiation_type, property_type
ORDER BY
    negotiation_type, avg_size DESC;


-- Proporção de propriedades com/sem mobílias para aluguel e venda:
SELECT
    negotiation_type,
    furnished,
    COUNT(*) AS count_properties
FROM
    raw
GROUP BY
    negotiation_type, furnished
ORDER BY negotiation_type;